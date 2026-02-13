/*****************************************************************************
  TRUST COMPONENTS
  
  (C) Trustserver S. L., 2009
  
  Todos los derechos reservados.
  
  $Id: hdr.h 116 2009-10-11 14:49:18Z bruno $
  $URL: https://svn.trustserver.net/svn/trabajo/componentes/trunk/include/hdr.h $
*****************************************************************************/

#ifndef __HDR_H__
#define __HDR_H__

#ifdef __GNUC__
#define ID_URL(t) static const char *ident_url __attribute__((unused)) = t 
#define ID_ID(t) static const char *ident_id __attribute__((unused)) = t 
#else
#define ID_URL(t) static const char *ident_url = t 
#define ID_ID(t) static const char *ident_id = t 
#endif

#endif // __HDR_H__

