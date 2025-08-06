class vehicles
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\vehicles\fnc";
	#else
	file = "mcc\vehicles\fnc";
	#endif

	//class BISGarage {description = "替换BI的车库功能，用于宙斯模式，所有功劳归宙斯";};
	class pylonsChange {description = "更改可用飞机的挂载配置";};
	class spawnVehicle {description = "替换BIS_fnc_spawnVehicle";};
	class vehicleRandomAnimation {description = "为车辆生成随机动画";};
	class addComponentsACECondition {description = "检查该车辆是否有可用的组件";};
	class addComponentsACE {description = "将组件子项添加到ACE";};
	class vehicleTireChange {description = "拆卸或安装车辆的轮胎或卡车";};
	class vehicleEngine {description = "打开或关闭车辆引擎，并通过循环强制保持状态，直到车辆被摧毁或设置变量MCCunitEngine为2";};
	class vehicleLights {description = "打开或关闭车辆灯光，并通过循环强制保持状态，直到车辆被摧毁或设置变量MCCunitEngine为2";};
	class vehicleService {description = "为给定车辆进行重新武装、修理和加油";};
};