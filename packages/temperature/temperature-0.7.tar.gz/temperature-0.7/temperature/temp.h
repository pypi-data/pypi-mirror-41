namespace TEMP {
    #include "Temperature.h"
}

// 1. auto_set
static int get_temp() {
	if (TEMP::GetTempCount() >= 1) {
		int value = TEMP::GetTemp1();
		if (0 < value && value < 1000) {
			return value;
		}
	}
	return -1;
}
