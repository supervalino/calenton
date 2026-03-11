from PyQt6.QtCore import QAbstractTableModel, Qt


class DatoTabular(QAbstractTableModel):
    """Stub: DatoTabular (dato tabular/series) — not yet implemented."""

    def __init__(self, parent=None, idFuente=None, db=None):
        super().__init__(parent)
        self._idFuente = idFuente

    def rowCount(self, parent=None):
        return 0

    def columnCount(self, parent=None):
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        return None

    def setIdFuente(self, idFuente):
        self._idFuente = idFuente
        self.beginResetModel()
        self.endResetModel()
