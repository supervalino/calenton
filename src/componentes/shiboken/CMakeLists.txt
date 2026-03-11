cmake_minimum_required(VERSION 3.18)
project(ts_bindings)

# ──────────────────────────────────────────────────────────────────────────────
# Options
# ──────────────────────────────────────────────────────────────────────────────
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Allow the caller to tell us where the installed componentes library lives.
# Default: look next to the build tree in a conventional layout.
if(NOT DEFINED COMPONENTES_ROOT)
    set(COMPONENTES_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/..")
endif()

# ──────────────────────────────────────────────────────────────────────────────
# Find Qt6
# ──────────────────────────────────────────────────────────────────────────────
find_package(Qt6 REQUIRED COMPONENTS Core Gui Sql Xml Widgets)

# ──────────────────────────────────────────────────────────────────────────────
# Find Shiboken6 / PySide6
# ──────────────────────────────────────────────────────────────────────────────
find_package(Shiboken6 REQUIRED)
find_package(PySide6 REQUIRED)

# Python interpreter / headers needed to build the extension module
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# ──────────────────────────────────────────────────────────────────────────────
# Locate the pre-built componentes library
# ──────────────────────────────────────────────────────────────────────────────
find_library(
    COMPONENTES_LIBRARY
    NAMES componentes
    HINTS "${COMPONENTES_ROOT}/lib" "${COMPONENTES_ROOT}"
    REQUIRED
)

# Public headers of the componentes library
set(COMPONENTES_INCLUDE_DIRS
    "${COMPONENTES_ROOT}/include"
    "${COMPONENTES_ROOT}/ui_include"
)

# ──────────────────────────────────────────────────────────────────────────────
# Paths used by Shiboken6
# ──────────────────────────────────────────────────────────────────────────────
# Location of Shiboken6's own typesystem XML files
get_target_property(SHIBOKEN_GENERATOR Shiboken6::shiboken6 LOCATION)
get_filename_component(SHIBOKEN_GENERATOR_DIR "${SHIBOKEN_GENERATOR}" DIRECTORY)

# PySide6 typesystem XML files are installed alongside PySide6
get_target_property(PYSIDE6_INCLUDE_DIR PySide6::pyside6 INTERFACE_INCLUDE_DIRECTORIES)
# Walk up one level to find typesystem XML files that ship with PySide6
get_filename_component(PYSIDE6_TYPESYSTEMS_DIR "${PYSIDE6_INCLUDE_DIR}/.." ABSOLUTE)

# ──────────────────────────────────────────────────────────────────────────────
# Shiboken generator invocation
# ──────────────────────────────────────────────────────────────────────────────
set(TYPESYSTEM_FILE "${CMAKE_CURRENT_SOURCE_DIR}/typesystem_ts.xml")
set(GLOBAL_HEADER   "${CMAKE_CURRENT_SOURCE_DIR}/global.h")
set(GENERATED_DIR   "${CMAKE_CURRENT_BINARY_DIR}/ts_generated")

file(MAKE_DIRECTORY "${GENERATED_DIR}")

# Collect all include paths for the generator's preprocessor
set(GENERATOR_INCLUDE_PATHS
    ${COMPONENTES_INCLUDE_DIRS}
    ${Qt6Core_INCLUDE_DIRS}
    ${Qt6Gui_INCLUDE_DIRS}
    ${Qt6Sql_INCLUDE_DIRS}
    ${Qt6Xml_INCLUDE_DIRS}
    ${Qt6Widgets_INCLUDE_DIRS}
    ${Python3_INCLUDE_DIRS}
)

# Build the -I flags string for shiboken6
foreach(_dir ${GENERATOR_INCLUDE_PATHS})
    list(APPEND GENERATOR_INCLUDE_FLAGS "-I${_dir}")
endforeach()

# Typesystem search path: PySide6 typesystem XMLs + current source dir
set(TYPESYSTEM_PATHS
    "${PYSIDE6_TYPESYSTEMS_DIR}"
    "${CMAKE_CURRENT_SOURCE_DIR}"
)
string(REPLACE ";" ":" TYPESYSTEM_PATHS_STR "${TYPESYSTEM_PATHS}")

# Enumerate generated source files so CMake can track them
# (shiboken6 generates one .cpp per exposed class plus a module registration)
set(GENERATED_SOURCES
    "${GENERATED_DIR}/ts_module_wrapper.cpp"
    "${GENERATED_DIR}/baseforeignkey_wrapper.cpp"
    "${GENERATED_DIR}/foreignkey_wrapper.cpp"
    "${GENERATED_DIR}/fkmodel_wrapper.cpp"
    "${GENERATED_DIR}/seqtablemodel_wrapper.cpp"
    "${GENERATED_DIR}/rowcontrol_wrapper.cpp"
    "${GENERATED_DIR}/rowcontrolchild_wrapper.cpp"
    "${GENERATED_DIR}/rowcontrolchildcolumnproxy_wrapper.cpp"
    "${GENERATED_DIR}/relone2one_wrapper.cpp"
    "${GENERATED_DIR}/relone2oneproxy_wrapper.cpp"
    "${GENERATED_DIR}/combodatamodel_wrapper.cpp"
    "${GENERATED_DIR}/dimension_wrapper.cpp"
    "${GENERATED_DIR}/magnitude_wrapper.cpp"
    "${GENERATED_DIR}/unit_wrapper.cpp"
    "${GENERATED_DIR}/unitcollection_wrapper.cpp"
    "${GENERATED_DIR}/unitsystem_wrapper.cpp"
    "${GENERATED_DIR}/datadialog_wrapper.cpp"
    "${GENERATED_DIR}/ttableview_wrapper.cpp"
    "${GENERATED_DIR}/tcombobox_wrapper.cpp"
    "${GENERATED_DIR}/ttabwidget_wrapper.cpp"
    "${GENERATED_DIR}/fkitemdelegate_wrapper.cpp"
    "${GENERATED_DIR}/dimensionedit_wrapper.cpp"
    "${GENERATED_DIR}/tsqlbuttonbox_wrapper.cpp"
    "${GENERATED_DIR}/tsqltablenavigator_wrapper.cpp"
)

add_custom_command(
    OUTPUT  ${GENERATED_SOURCES}
    COMMAND "${SHIBOKEN_GENERATOR}"
            --generator-set=shiboken
            --enable-parent-ctor-heuristic
            --enable-return-value-heuristic
            --use-isnull-as-nb_nonzero
            ${GENERATOR_INCLUDE_FLAGS}
            "--typesystem-paths=${TYPESYSTEM_PATHS_STR}"
            "--output-directory=${GENERATED_DIR}"
            "${GLOBAL_HEADER}"
            "${TYPESYSTEM_FILE}"
    DEPENDS "${GLOBAL_HEADER}" "${TYPESYSTEM_FILE}"
    COMMENT "Generating Python bindings for the ts module with Shiboken6"
    VERBATIM
)

add_custom_target(generate_ts_bindings DEPENDS ${GENERATED_SOURCES})

# ──────────────────────────────────────────────────────────────────────────────
# Build the Python extension module
# ──────────────────────────────────────────────────────────────────────────────
Python3_add_library(ts MODULE ${GENERATED_SOURCES})

add_dependencies(ts generate_ts_bindings)

target_include_directories(ts
    PRIVATE
        ${COMPONENTES_INCLUDE_DIRS}
        ${GENERATED_DIR}/ts
        ${Qt6Core_INCLUDE_DIRS}
        ${Qt6Gui_INCLUDE_DIRS}
        ${Qt6Sql_INCLUDE_DIRS}
        ${Qt6Xml_INCLUDE_DIRS}
        ${Qt6Widgets_INCLUDE_DIRS}
        ${Python3_INCLUDE_DIRS}
)

target_link_libraries(ts
    PRIVATE
        "${COMPONENTES_LIBRARY}"
        Qt6::Core
        Qt6::Gui
        Qt6::Sql
        Qt6::Xml
        Qt6::Widgets
        Shiboken6::libshiboken
        PySide6::pyside6
        Python3::Python
)

# Extension modules must not have a "lib" prefix on Linux
set_target_properties(ts PROPERTIES PREFIX "")

# ──────────────────────────────────────────────────────────────────────────────
# Install
# ──────────────────────────────────────────────────────────────────────────────
if(NOT DEFINED TS_INSTALL_DIR)
    # Default: put the module where Python can find it
    execute_process(
        COMMAND "${Python3_EXECUTABLE}" -c
            "import sysconfig; print(sysconfig.get_path('platlib'))"
        OUTPUT_VARIABLE _PYTHON_PLATLIB
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    set(TS_INSTALL_DIR "${_PYTHON_PLATLIB}")
endif()

install(TARGETS ts DESTINATION "${TS_INSTALL_DIR}")
