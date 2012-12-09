# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hydraharp_comm', [dirname(__file__)])
        except ImportError:
            import _hydraharp_comm
            return _hydraharp_comm
        if fp is not None:
            try:
                _mod = imp.load_module('_hydraharp_comm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _hydraharp_comm = swig_import_helper()
    del swig_import_helper
else:
    import _hydraharp_comm
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _hydraharp_comm.new_intp()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _hydraharp_comm.delete_intp
    __del__ = lambda self : None;
    def assign(self, *args): return _hydraharp_comm.intp_assign(self, *args)
    def value(self): return _hydraharp_comm.intp_value(self)
    def cast(self): return _hydraharp_comm.intp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _hydraharp_comm.intp_frompointer
    if _newclass:frompointer = staticmethod(_hydraharp_comm.intp_frompointer)
intp_swigregister = _hydraharp_comm.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(*args):
  return _hydraharp_comm.intp_frompointer(*args)
intp_frompointer = _hydraharp_comm.intp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _hydraharp_comm.new_doublep()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _hydraharp_comm.delete_doublep
    __del__ = lambda self : None;
    def assign(self, *args): return _hydraharp_comm.doublep_assign(self, *args)
    def value(self): return _hydraharp_comm.doublep_value(self)
    def cast(self): return _hydraharp_comm.doublep_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _hydraharp_comm.doublep_frompointer
    if _newclass:frompointer = staticmethod(_hydraharp_comm.doublep_frompointer)
doublep_swigregister = _hydraharp_comm.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(*args):
  return _hydraharp_comm.doublep_frompointer(*args)
doublep_frompointer = _hydraharp_comm.doublep_frompointer

class uint_array(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, uint_array, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, uint_array, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _hydraharp_comm.new_uint_array(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _hydraharp_comm.delete_uint_array
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _hydraharp_comm.uint_array___getitem__(self, *args)
    def __setitem__(self, *args): return _hydraharp_comm.uint_array___setitem__(self, *args)
    def cast(self): return _hydraharp_comm.uint_array_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _hydraharp_comm.uint_array_frompointer
    if _newclass:frompointer = staticmethod(_hydraharp_comm.uint_array_frompointer)
uint_array_swigregister = _hydraharp_comm.uint_array_swigregister
uint_array_swigregister(uint_array)

def uint_array_frompointer(*args):
  return _hydraharp_comm.uint_array_frompointer(*args)
uint_array_frompointer = _hydraharp_comm.uint_array_frompointer

HH_ERROR_NONE = _hydraharp_comm.HH_ERROR_NONE
HH_ERROR_DEVICE_OPEN_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_OPEN_FAIL
HH_ERROR_DEVICE_BUSY = _hydraharp_comm.HH_ERROR_DEVICE_BUSY
HH_ERROR_DEVICE_HEVENT_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_HEVENT_FAIL
HH_ERROR_DEVICE_CALLBSET_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_CALLBSET_FAIL
HH_ERROR_DEVICE_BARMAP_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_BARMAP_FAIL
HH_ERROR_DEVICE_CLOSE_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_CLOSE_FAIL
HH_ERROR_DEVICE_RESET_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_RESET_FAIL
HH_ERROR_DEVICE_GETVERSION_FAIL = _hydraharp_comm.HH_ERROR_DEVICE_GETVERSION_FAIL
HH_ERROR_DEVICE_VERSION_MISMATCH = _hydraharp_comm.HH_ERROR_DEVICE_VERSION_MISMATCH
HH_ERROR_DEVICE_NOT_OPEN = _hydraharp_comm.HH_ERROR_DEVICE_NOT_OPEN
HH_ERROR_INSTANCE_RUNNING = _hydraharp_comm.HH_ERROR_INSTANCE_RUNNING
HH_ERROR_INVALID_ARGUMENT = _hydraharp_comm.HH_ERROR_INVALID_ARGUMENT
HH_ERROR_INVALID_MODE = _hydraharp_comm.HH_ERROR_INVALID_MODE
HH_ERROR_INVALID_OPTION = _hydraharp_comm.HH_ERROR_INVALID_OPTION
HH_ERROR_INVALID_MEMORY = _hydraharp_comm.HH_ERROR_INVALID_MEMORY
HH_ERROR_INVALID_RDATA = _hydraharp_comm.HH_ERROR_INVALID_RDATA
HH_ERROR_NOT_INITIALIZED = _hydraharp_comm.HH_ERROR_NOT_INITIALIZED
HH_ERROR_NOT_CALIBRATED = _hydraharp_comm.HH_ERROR_NOT_CALIBRATED
HH_ERROR_DMA_FAIL = _hydraharp_comm.HH_ERROR_DMA_FAIL
HH_ERROR_XTDEVICE_FAIL = _hydraharp_comm.HH_ERROR_XTDEVICE_FAIL
HH_ERROR_FPGACONF_FAIL = _hydraharp_comm.HH_ERROR_FPGACONF_FAIL
HH_ERROR_IFCONF_FAIL = _hydraharp_comm.HH_ERROR_IFCONF_FAIL
HH_ERROR_FIFORESET_FAIL = _hydraharp_comm.HH_ERROR_FIFORESET_FAIL
HH_ERROR_USB_GETDRIVERVER_FAIL = _hydraharp_comm.HH_ERROR_USB_GETDRIVERVER_FAIL
HH_ERROR_USB_DRIVERVER_MISMATCH = _hydraharp_comm.HH_ERROR_USB_DRIVERVER_MISMATCH
HH_ERROR_USB_GETIFINFO_FAIL = _hydraharp_comm.HH_ERROR_USB_GETIFINFO_FAIL
HH_ERROR_USB_HISPEED_FAIL = _hydraharp_comm.HH_ERROR_USB_HISPEED_FAIL
HH_ERROR_USB_VCMD_FAIL = _hydraharp_comm.HH_ERROR_USB_VCMD_FAIL
HH_ERROR_USB_BULKRD_FAIL = _hydraharp_comm.HH_ERROR_USB_BULKRD_FAIL
HH_ERROR_USB_RESET_FAIL = _hydraharp_comm.HH_ERROR_USB_RESET_FAIL
HH_ERROR_LANEUP_TIMEOUT = _hydraharp_comm.HH_ERROR_LANEUP_TIMEOUT
HH_ERROR_DONEALL_TIMEOUT = _hydraharp_comm.HH_ERROR_DONEALL_TIMEOUT
HH_ERROR_MODACK_TIMEOUT = _hydraharp_comm.HH_ERROR_MODACK_TIMEOUT
HH_ERROR_MACTIVE_TIMEOUT = _hydraharp_comm.HH_ERROR_MACTIVE_TIMEOUT
HH_ERROR_MEMCLEAR_FAIL = _hydraharp_comm.HH_ERROR_MEMCLEAR_FAIL
HH_ERROR_MEMTEST_FAIL = _hydraharp_comm.HH_ERROR_MEMTEST_FAIL
HH_ERROR_CALIB_FAIL = _hydraharp_comm.HH_ERROR_CALIB_FAIL
HH_ERROR_REFSEL_FAIL = _hydraharp_comm.HH_ERROR_REFSEL_FAIL
HH_ERROR_STATUS_FAIL = _hydraharp_comm.HH_ERROR_STATUS_FAIL
HH_ERROR_MODNUM_FAIL = _hydraharp_comm.HH_ERROR_MODNUM_FAIL
HH_ERROR_DIGMUX_FAIL = _hydraharp_comm.HH_ERROR_DIGMUX_FAIL
HH_ERROR_MODMUX_FAIL = _hydraharp_comm.HH_ERROR_MODMUX_FAIL
HH_ERROR_MODFWPCB_MISMATCH = _hydraharp_comm.HH_ERROR_MODFWPCB_MISMATCH
HH_ERROR_MODFWVER_MISMATCH = _hydraharp_comm.HH_ERROR_MODFWVER_MISMATCH
HH_ERROR_MODPROPERTY_MISMATCH = _hydraharp_comm.HH_ERROR_MODPROPERTY_MISMATCH
HH_ERROR_INVALID_MAGIC = _hydraharp_comm.HH_ERROR_INVALID_MAGIC
HH_ERROR_INVALID_LENGTH = _hydraharp_comm.HH_ERROR_INVALID_LENGTH
HH_ERROR_RATE_FAIL = _hydraharp_comm.HH_ERROR_RATE_FAIL
HH_ERROR_MODFWVER_TOO_LOW = _hydraharp_comm.HH_ERROR_MODFWVER_TOO_LOW
HH_ERROR_MODFWVER_TOO_HIGH = _hydraharp_comm.HH_ERROR_MODFWVER_TOO_HIGH
HH_ERROR_EEPROM_F01 = _hydraharp_comm.HH_ERROR_EEPROM_F01
HH_ERROR_EEPROM_F02 = _hydraharp_comm.HH_ERROR_EEPROM_F02
HH_ERROR_EEPROM_F03 = _hydraharp_comm.HH_ERROR_EEPROM_F03
HH_ERROR_EEPROM_F04 = _hydraharp_comm.HH_ERROR_EEPROM_F04
HH_ERROR_EEPROM_F05 = _hydraharp_comm.HH_ERROR_EEPROM_F05
HH_ERROR_EEPROM_F06 = _hydraharp_comm.HH_ERROR_EEPROM_F06
HH_ERROR_EEPROM_F07 = _hydraharp_comm.HH_ERROR_EEPROM_F07
HH_ERROR_EEPROM_F08 = _hydraharp_comm.HH_ERROR_EEPROM_F08
HH_ERROR_EEPROM_F09 = _hydraharp_comm.HH_ERROR_EEPROM_F09
HH_ERROR_EEPROM_F10 = _hydraharp_comm.HH_ERROR_EEPROM_F10
HH_ERROR_EEPROM_F11 = _hydraharp_comm.HH_ERROR_EEPROM_F11
LIB_VERSION = _hydraharp_comm.LIB_VERSION
MAXDEVNUM = _hydraharp_comm.MAXDEVNUM
HHMAXINPCHAN = _hydraharp_comm.HHMAXINPCHAN
MAXBINSTEPS = _hydraharp_comm.MAXBINSTEPS
MAXHISTLEN = _hydraharp_comm.MAXHISTLEN
MAXLENCODE = _hydraharp_comm.MAXLENCODE
MAXHISTLEN_CONT = _hydraharp_comm.MAXHISTLEN_CONT
MAXLENCODE_CONT = _hydraharp_comm.MAXLENCODE_CONT
TTREADMAX = _hydraharp_comm.TTREADMAX
TTREADMIN = _hydraharp_comm.TTREADMIN
MODE_HIST = _hydraharp_comm.MODE_HIST
MODE_T2 = _hydraharp_comm.MODE_T2
MODE_T3 = _hydraharp_comm.MODE_T3
MODE_CONT = _hydraharp_comm.MODE_CONT
MEASCTRL_SINGLESHOT_CTC = _hydraharp_comm.MEASCTRL_SINGLESHOT_CTC
MEASCTRL_C1_GATED = _hydraharp_comm.MEASCTRL_C1_GATED
MEASCTRL_C1_START_CTC_STOP = _hydraharp_comm.MEASCTRL_C1_START_CTC_STOP
MEASCTRL_C1_START_C2_STOP = _hydraharp_comm.MEASCTRL_C1_START_C2_STOP
MEASCTRL_CONT_C1_GATED = _hydraharp_comm.MEASCTRL_CONT_C1_GATED
MEASCTRL_CONT_C1_START_CTC_STOP = _hydraharp_comm.MEASCTRL_CONT_C1_START_CTC_STOP
MEASCTRL_CONT_CTC_RESTART = _hydraharp_comm.MEASCTRL_CONT_CTC_RESTART
EDGE_RISING = _hydraharp_comm.EDGE_RISING
EDGE_FALLING = _hydraharp_comm.EDGE_FALLING
FLAG_OVERFLOW = _hydraharp_comm.FLAG_OVERFLOW
FLAG_FIFOFULL = _hydraharp_comm.FLAG_FIFOFULL
FLAG_SYNC_LOST = _hydraharp_comm.FLAG_SYNC_LOST
FLAG_REF_LOST = _hydraharp_comm.FLAG_REF_LOST
FLAG_SYSERROR = _hydraharp_comm.FLAG_SYSERROR
FLAG_ACTIVE = _hydraharp_comm.FLAG_ACTIVE
SYNCDIVMIN = _hydraharp_comm.SYNCDIVMIN
SYNCDIVMAX = _hydraharp_comm.SYNCDIVMAX
ZCMIN = _hydraharp_comm.ZCMIN
ZCMAX = _hydraharp_comm.ZCMAX
DISCRMIN = _hydraharp_comm.DISCRMIN
DISCRMAX = _hydraharp_comm.DISCRMAX
CHANOFFSMIN = _hydraharp_comm.CHANOFFSMIN
CHANOFFSMAX = _hydraharp_comm.CHANOFFSMAX
OFFSETMIN = _hydraharp_comm.OFFSETMIN
OFFSETMAX = _hydraharp_comm.OFFSETMAX
ACQTMIN = _hydraharp_comm.ACQTMIN
ACQTMAX = _hydraharp_comm.ACQTMAX
STOPCNTMIN = _hydraharp_comm.STOPCNTMIN
STOPCNTMAX = _hydraharp_comm.STOPCNTMAX
WARNING_SYNC_RATE_ZERO = _hydraharp_comm.WARNING_SYNC_RATE_ZERO
WARNING_SYNC_RATE_TOO_LOW = _hydraharp_comm.WARNING_SYNC_RATE_TOO_LOW
WARNING_SYNC_RATE_TOO_HIGH = _hydraharp_comm.WARNING_SYNC_RATE_TOO_HIGH
WARNING_INPT_RATE_ZERO = _hydraharp_comm.WARNING_INPT_RATE_ZERO
WARNING_INPT_RATE_TOO_HIGH = _hydraharp_comm.WARNING_INPT_RATE_TOO_HIGH
WARNING_INPT_RATE_RATIO = _hydraharp_comm.WARNING_INPT_RATE_RATIO
WARNING_DIVIDER_GREATER_ONE = _hydraharp_comm.WARNING_DIVIDER_GREATER_ONE
WARNING_TIME_SPAN_TOO_SMALL = _hydraharp_comm.WARNING_TIME_SPAN_TOO_SMALL
WARNING_OFFSET_UNNECESSARY = _hydraharp_comm.WARNING_OFFSET_UNNECESSARY

def HH_GetLibraryVersion(*args):
  return _hydraharp_comm.HH_GetLibraryVersion(*args)
HH_GetLibraryVersion = _hydraharp_comm.HH_GetLibraryVersion

def HH_GetErrorString(*args):
  return _hydraharp_comm.HH_GetErrorString(*args)
HH_GetErrorString = _hydraharp_comm.HH_GetErrorString

def HH_OpenDevice(*args):
  return _hydraharp_comm.HH_OpenDevice(*args)
HH_OpenDevice = _hydraharp_comm.HH_OpenDevice

def HH_CloseDevice(*args):
  return _hydraharp_comm.HH_CloseDevice(*args)
HH_CloseDevice = _hydraharp_comm.HH_CloseDevice

def HH_Initialize(*args):
  return _hydraharp_comm.HH_Initialize(*args)
HH_Initialize = _hydraharp_comm.HH_Initialize

def HH_GetHardwareInfo(*args):
  return _hydraharp_comm.HH_GetHardwareInfo(*args)
HH_GetHardwareInfo = _hydraharp_comm.HH_GetHardwareInfo

def HH_GetSerialNumber(*args):
  return _hydraharp_comm.HH_GetSerialNumber(*args)
HH_GetSerialNumber = _hydraharp_comm.HH_GetSerialNumber

def HH_GetBaseResolution(*args):
  return _hydraharp_comm.HH_GetBaseResolution(*args)
HH_GetBaseResolution = _hydraharp_comm.HH_GetBaseResolution

def HH_GetNumOfInputChannels(*args):
  return _hydraharp_comm.HH_GetNumOfInputChannels(*args)
HH_GetNumOfInputChannels = _hydraharp_comm.HH_GetNumOfInputChannels

def HH_GetNumOfModules(*args):
  return _hydraharp_comm.HH_GetNumOfModules(*args)
HH_GetNumOfModules = _hydraharp_comm.HH_GetNumOfModules

def HH_GetModuleInfo(*args):
  return _hydraharp_comm.HH_GetModuleInfo(*args)
HH_GetModuleInfo = _hydraharp_comm.HH_GetModuleInfo

def HH_GetModuleIndex(*args):
  return _hydraharp_comm.HH_GetModuleIndex(*args)
HH_GetModuleIndex = _hydraharp_comm.HH_GetModuleIndex

def HH_Calibrate(*args):
  return _hydraharp_comm.HH_Calibrate(*args)
HH_Calibrate = _hydraharp_comm.HH_Calibrate

def HH_SetSyncDiv(*args):
  return _hydraharp_comm.HH_SetSyncDiv(*args)
HH_SetSyncDiv = _hydraharp_comm.HH_SetSyncDiv

def HH_SetSyncCFD(*args):
  return _hydraharp_comm.HH_SetSyncCFD(*args)
HH_SetSyncCFD = _hydraharp_comm.HH_SetSyncCFD

def HH_SetSyncChannelOffset(*args):
  return _hydraharp_comm.HH_SetSyncChannelOffset(*args)
HH_SetSyncChannelOffset = _hydraharp_comm.HH_SetSyncChannelOffset

def HH_SetInputCFD(*args):
  return _hydraharp_comm.HH_SetInputCFD(*args)
HH_SetInputCFD = _hydraharp_comm.HH_SetInputCFD

def HH_SetInputChannelOffset(*args):
  return _hydraharp_comm.HH_SetInputChannelOffset(*args)
HH_SetInputChannelOffset = _hydraharp_comm.HH_SetInputChannelOffset

def HH_SetInputChannelEnable(*args):
  return _hydraharp_comm.HH_SetInputChannelEnable(*args)
HH_SetInputChannelEnable = _hydraharp_comm.HH_SetInputChannelEnable

def HH_SetStopOverflow(*args):
  return _hydraharp_comm.HH_SetStopOverflow(*args)
HH_SetStopOverflow = _hydraharp_comm.HH_SetStopOverflow

def HH_SetBinning(*args):
  return _hydraharp_comm.HH_SetBinning(*args)
HH_SetBinning = _hydraharp_comm.HH_SetBinning

def HH_SetOffset(*args):
  return _hydraharp_comm.HH_SetOffset(*args)
HH_SetOffset = _hydraharp_comm.HH_SetOffset

def HH_SetHistoLen(*args):
  return _hydraharp_comm.HH_SetHistoLen(*args)
HH_SetHistoLen = _hydraharp_comm.HH_SetHistoLen

def HH_SetMeasControl(*args):
  return _hydraharp_comm.HH_SetMeasControl(*args)
HH_SetMeasControl = _hydraharp_comm.HH_SetMeasControl

def HH_ClearHistMem(*args):
  return _hydraharp_comm.HH_ClearHistMem(*args)
HH_ClearHistMem = _hydraharp_comm.HH_ClearHistMem

def HH_StartMeas(*args):
  return _hydraharp_comm.HH_StartMeas(*args)
HH_StartMeas = _hydraharp_comm.HH_StartMeas

def HH_StopMeas(*args):
  return _hydraharp_comm.HH_StopMeas(*args)
HH_StopMeas = _hydraharp_comm.HH_StopMeas

def HH_CTCStatus(*args):
  return _hydraharp_comm.HH_CTCStatus(*args)
HH_CTCStatus = _hydraharp_comm.HH_CTCStatus

def HH_GetHistogram(*args):
  return _hydraharp_comm.HH_GetHistogram(*args)
HH_GetHistogram = _hydraharp_comm.HH_GetHistogram

def HH_GetResolution(*args):
  return _hydraharp_comm.HH_GetResolution(*args)
HH_GetResolution = _hydraharp_comm.HH_GetResolution

def HH_GetSyncRate(*args):
  return _hydraharp_comm.HH_GetSyncRate(*args)
HH_GetSyncRate = _hydraharp_comm.HH_GetSyncRate

def HH_GetCountRate(*args):
  return _hydraharp_comm.HH_GetCountRate(*args)
HH_GetCountRate = _hydraharp_comm.HH_GetCountRate

def HH_GetFlags(*args):
  return _hydraharp_comm.HH_GetFlags(*args)
HH_GetFlags = _hydraharp_comm.HH_GetFlags

def HH_GetElapsedMeasTime(*args):
  return _hydraharp_comm.HH_GetElapsedMeasTime(*args)
HH_GetElapsedMeasTime = _hydraharp_comm.HH_GetElapsedMeasTime

def HH_GetWarnings(*args):
  return _hydraharp_comm.HH_GetWarnings(*args)
HH_GetWarnings = _hydraharp_comm.HH_GetWarnings

def HH_GetWarningsText(*args):
  return _hydraharp_comm.HH_GetWarningsText(*args)
HH_GetWarningsText = _hydraharp_comm.HH_GetWarningsText

def HH_SetMarkerHoldoff(*args):
  return _hydraharp_comm.HH_SetMarkerHoldoff(*args)
HH_SetMarkerHoldoff = _hydraharp_comm.HH_SetMarkerHoldoff

def HH_SetMarkerEdges(*args):
  return _hydraharp_comm.HH_SetMarkerEdges(*args)
HH_SetMarkerEdges = _hydraharp_comm.HH_SetMarkerEdges

def HH_SetMarkerEnable(*args):
  return _hydraharp_comm.HH_SetMarkerEnable(*args)
HH_SetMarkerEnable = _hydraharp_comm.HH_SetMarkerEnable

def HH_ReadFiFo(*args):
  return _hydraharp_comm.HH_ReadFiFo(*args)
HH_ReadFiFo = _hydraharp_comm.HH_ReadFiFo

def HH_GetContModeBlock(*args):
  return _hydraharp_comm.HH_GetContModeBlock(*args)
HH_GetContModeBlock = _hydraharp_comm.HH_GetContModeBlock
# This file is compatible with both classic and new-style classes.

