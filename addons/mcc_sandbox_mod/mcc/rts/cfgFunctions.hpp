class rts
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\rts\fnc";
	#else
	file = "mcc\rts\fnc";
	#endif

	class boxMakeWeaponsArray {};
	class addVirtualItemCargo {};
	class addVirtualWeaponCargo {};
	class addVirtualMagazineCargo {};
	class getVirtualItemCargo {};
	class getVirtualWeaponCargo {};
	class getVirtualMagazineCargo {};
	class removeVirtualItemCargo {};
	class removeVirtualWeaponCargo {};
	class removeVirtualMagazineCargo {};
	class baseResourceReduce {};
	class baseSelected {};
	class rtsClearBuilding {};
	class baseActionClicked {};
	class baseActionEntered {};
	class baseActionExit {};
	class baseOpenConstMenu {};
	class baseBuildBorders {};
	class CheckRes {};
	class CheckBuildings {};
	class mainBoxOpen {};
	class vehicleSpawnerInit {};
	class vehicleSpawner {};
	class makeObjectVirtualBox {};
	class rtsMountGuns {description = "为民用载具安装炮塔";};
	class initWorkshop {description = "初始化车间类建筑";};
	class rtsStartElectricity {description = "开始发电";};
	class rtsScanResourcesCancel {description = "取消资源任务";};
	class rtsScanResources {description = "生成资源任务";};
	class rtsBuyTickets {description = "添加票券";};
	class rtsCreateMeds {description = "创建药品";};
	class rtsUpgrade {description = "升级建筑";};
	class rtsDestroyLogic {description = "摧毁选定的逻辑";};
	class rtsDestroyObject {description = "摧毁选定的对象";};
	class rtsPopulateVehicle {description = "填充载具";};
	class vehicleSpawnerInitDialog {description = "打开载具生成器对话框";};
	class rtsBuildUIContainer {description = "创建一个UI容器";};
	class rtsBuildUIContainerBack {description = "从UI容器返回";};
	class rtsbuyVehicle {description = "为指挥官打开载具生成器对话框";};
	class rtsOrderStop {description = "停止行动";};
	class rtsOrderGetout {description = "命令单位下车";};
	class rtsOrderLand {description = "命令降落";};
	class rtsTradeforFood {description = "用资源换取食物";};
	class rtsCreateGroup {description = "生成单位组";};
	class rtsLoadResources {description = "装载后勤物资箱";};
	class rtsLoadResourcesAmmo {description = "提取弹药箱";};
	class rtsLoadResourcesSupply {description = "提取补给箱";};
	class rtsLoadResourcesFuel {description = "提取燃料箱";};
	class rtsUnloadResources {description = "卸载后勤物资箱";};
	class rtsBuildingProgress {description = "管理建筑进度";};
	class rtsIsRespawnUnits{description = "检查是否可以复活单位";};
	class rtsRespawnUnits {description = "复活组内死亡的单位";};
	class rtsOrderPlaceSatchel {description = "放置炸药包";};
	class rtsTakeControl {description = "远程控制选定单位";};
	class mainBoxInit {};
	class saveCargoBox {description = "使用iniDB从服务器保存或加载货物箱物品";};
	class rtsaddArtilleryAmmo {description = "购买10发炮弹";};
	class rtsCalculateResourceTreshold {description = "计算资源阈值";};
	class getWeaponCost {description = "根据武器的有效DPS、射程和弹药获取武器成本";};
	class rtsEvacHelicopterBuy {description = "如果不可用则生成一架撤离直升机";};
	class getVehicleCost {description = "返回载具成本——载具终端的一部分";};
	class vehicleSpawnerBuildCostTable {description = "为载具终端构建成本表";};
};

class forts
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\rts\fnc\forts";
	#else
	file = "mcc\rts\fnc\forts";
	#endif

	class buildFort {};
};

class missions
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\rts\fnc\missions";
	#else
	file = "mcc\rts\fnc\missions";
	#endif

	class rtsScanResourcesBasic {description = "开始基础资源任务";};
	class rtsScanResourcesAdvanced {description = "开始高级资源任务";};
	class rtsInitmission {description = "情报收集任务";};
};