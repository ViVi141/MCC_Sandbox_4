class general
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\general";
	class pre_init
	{
		preInit = 1;
		description = "仅限模组的预初始化";
	};
	#else
	file = "mcc\fnc\general";
	#endif

	class login {};
	class activateAddons {preInit = 1; description = "预初始化插件";};
	class gear	{preInit = 1; description = "根据角色分配装备";};

	class mobileRespawn	{description = "当单位存活时，将重生标记移动到单位的当前位置；如果单位死亡，则将标记移动到之前的位置。";};
	class buildingPosCount	{description = "返回建筑物中索引位置的数量。";};
	class makeUnitsArray	{description = "返回一个单位数组，包含从给定函数和模拟中获取的所有单位，格式为[_cfgclass,_vehicleDisplayName]。";};
	class countGroup	{description = "计算组中的步兵、车辆、坦克、飞机、船只的数量。";};
	class PiPOpen	{description = "执行传输画面的动画。";};
	class time2String	{description = "将时间转换为字符串。";};
	class time	{description = "将时间转换为hh:mm:ss格式。";};
	class setVehicleInit	{description = "设置车辆初始化。";};
	class setVehicleName	{description = "设置车辆名称。";};
	class setTime	{description = "在所有客户端上设置时间。";};
	class setWeather	{description = "在所有客户端上设置天气 - 跳过一小时以使天气变化。";};
	class globalSay3D	{description = "在所有客户端上播放3D声音。";};
	class globalHint	{description = "在所有客户端上广播消息。";};
	class globalExecute	{description = "在选定的客户端或服务器上全局执行命令。";};
	class groupChat	{description = "在多人游戏中发送聊天消息。";};
	class moveToPos		{description = "将对象移动到新位置。";};
	class pickItem	{description = "使车辆类物品可拾取并为其添加变量。";};
	class broadcast	{description = "创建一个虚拟摄像机，并向所有客户端广播15秒的画中画视频。";};
	class paradrop	{description = "为给定单位创建HALO或常规跳伞。";};
	class realParadrop	{description = "为给定单位创建HALO或常规跳伞，并模拟从飞机中跳出的过程。";};
	class realParadropPlayer	{description = "从单位侧处理跳伞。";};
	class countGroupHC	{description = "计算组中的步兵、车辆、坦克、飞机、船只的数量（扩展版）。";};
	class manageWp	{description = "在地图上创建和控制AI路径点。";};
	class sync	{description = "将玩家与服务器同步。";};
	class objectMapper	{description = "获取动态对象模板的数据数组并创建对象。";};
	class findRoadsLeadingZone	{description = "找到通向某个区域的道路段。";};
	class nearestRoad	{description = "返回靠近位置的路径段数组";};
	class garrison	{description = "在空房子内布置士兵";};
	class saveToSQM	{description = "以SQM文件格式保存MCC的放置，并将其复制到剪贴板";};
	class saveToMCC	{description = "准备mcc_output变量";};
	class loadFromMCC	{description = "加载mcc_output变量";};
	class saveToComp	{description = "以组合格式保存MCC的3D编辑器放置";};
	class replaceString	{description = "过滤字符串并删除某些字符（_filter）";};
	class dirToString	{description = "获取方向整数并将其返回为字符串（北、东等）";};
	class startLocations	{description = "当找到起始位置时，传送玩家";};
	class spawnGroup	{description = "MCC自定义组生成";};
	class keyToName		{description = "获取idkKey并返回其名称的字符串";};
	class makeBriefing	{description = "仅限服务器 - 创建基于逻辑的任务简报";};
	class handleAddaction	{description = "处理重生后的添加动作 - 初始化";};
	class ppEffects	{description = "为所有玩家创建效果";};
	class SetPitchBankYaw	{};
	class openArtillery {};
	class deleteBrush{};
	class crewCount {description = "返回特定车辆的空座位数，包括或不包括FFV（车载射击）";};
	class addVelocity {description = "根据对象的当前速度为其添加速度";};
	class makeTask {description = "在服务器上使用BI的setTask函数处理任务";};
	class halt {description = "暂停游戏中的所有功能";};
};

class ied
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\ied";
	#else
	file = "mcc\fnc\ied";
	#endif

	class IedFakeExplosion	{description = "创建一个假IED。";};
	class IedDeadlyExplosion	{description = "创建一个致命的IED。";};
	class IedDisablingExplosion	{description = "创建一个致残的IED。";};
	class ACSingle	{description = "在给定位置创建一个武装平民。";};
	class trapSingle	{description = "在给定位置创建IED。";};
	class iedHit		{description = "确定当IED被击中时会发生什么。";};
	class ambushSingle	{description = "创建一个伏击小组。";};
	class createIED		{description = "创建IED机制。";};
	class manageAmbush	{description = "管理小组中的伏击行为。";};
	class manageAC		{description = "管理武装平民的行为。";};
	class SBSingle		{description = "放置自杀式炸弹袭击者。";};
	class manageSB		{description = "管理自杀式炸弹袭击者的行为。";};
	class mineSingle	{description = "创建一个雷区。";};
	class iedSync {};
};

class cas
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\cas";
	#else
	file = "mcc\fnc\cas";
	#endif

	class CreateAmmoDrop	{description = "从飞机上投下一个物体并为其附加降落伞，感谢BIS。";};
	class createPlane		{description = "从给定类型创建一个飞行中的飞机，并返回飞机、飞行员和小组。";};
	class deletePlane		{description = "设置飞机移动到某个位置，并在其接近800米时删除它。";};
	class airDrop		{description = "在服务器上处理CAS和空投请求";};
	class uavDetect {};
	class cas {description = "使用改装车辆模拟宙斯CAS";};
};

class artillery
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\artillery";
	#else
	file = "mcc\fnc\artillery";
	#endif

	class CBU	{description = "投下一枚炸弹，爆炸后分裂成多个带降落伞的小炸弹，再次爆炸形成某种CBU。";};
	class SADARM	{description = "投下一枚炸弹，爆炸后分裂成多个小炸弹，搜索并摧毁附近的装甲。";};
	class artyBomb	{description = "在给定位置创建带有声音的炮击。";};
	class artyFlare	{description = "创建一个照明弹。";};
	class artyDPICM	{description = "创建DPICM炮击弹幕。";};
	class amb_Art	{description = "创建环境炮击弹幕。";};
	class calcSolution	{description = "计算炮击解决方案（高或低）";};
	class artyGetSolution	{description = "广播炮击解决方案（高或低）";};
	class consoleFireArtillery	{description = "向炮兵单位广播炮击";};
	class artillery {};
};

class groupGen
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\groupGen";
	#else
	file = "mcc\fnc\groupGen";
	#endif

	class groupGenRefresh	{description = "刷新组生成标记";};
	class groupSpawn		{description = "在服务器上创建一个小组";};
	class groupGenUMRefresh	{description = "刷新组生成单位列表";};
};

class console
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\console";
	#else
	file = "mcc\fnc\console";
	#endif

	class consoleClickGroupIcon	{description = "定义MCC控制台中点击图标时的行为";};
};

class mp
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\mp";
	#else
	file = "mcc\fnc\mp";
	#endif

	class vote	{description = "启动投票过程。";};
	class getActiveSides	{description = "返回角色选择游戏中活跃阵营的数组。";};
	class PDAcreatemarker	{description = "在多人游戏中按阵营创建标记，并在一段时间后删除它们";};
	class construction		{description = "在服务器端建造战术建筑";};
	class construct_base	{description = "在基地中建造建筑";};
	class addRating			{description = "为特定玩家添加评分";};
	class radioSupport		{description = "向所有元素广播无线电支持，不包括广播者小组";};
	class inidbGet	{};
	class inidbSet 	{};
	class handleDB {};
	class saveServer {description = "将服务器的持久数据保存到服务器";};
	class loadServer {description = "从服务器加载服务器的持久数据";};
	class savePlayer {description = "将玩家的持久数据保存到服务器";};
	class loadPlayer {description = "从服务器加载玩家的持久数据";};
	class clearPersistentData {description = "清除所有保存文件中的数据";};
};

class actions
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\actions";
	#else
	file = "mcc\fnc\actions";
	#endif

	class ilsChilds		{description = "处理ILS子项";};
	class dragObject	{description = "开始拖动动画，必须在拖动单位本地运行";};
	class releaseObject	{description = "停止拖动动画，必须在拖动单位本地运行";};
	class releasePod	{description = "从Taru直升机上释放吊舱";};
	class attachPod		{description = "将吊舱附加到Taru直升机上";};
	class vault			{description = "翻越障碍物";};
	class cover			{description = "管理掩护机制";};
	class coverInit		{preInit = 1; description = "初始化掩护系统";};
	class weaponSelect	{description = "切换武器并投掷道具";};
	class utilityUse	{description = "使用道具";};
	class grenadeThrow	{description = "投掷手榴弹";};
	class pickKit		{description = "拾取死亡单位的装备";};
	class canAttachPod	{description = "检查是否可以附加吊舱";};
	class addILSChildrenACE {description = "将ILS动作添加到ACE UI";};
	class spotEnemy {description = "从ACE菜单中发现敌人";};
	class callSupport {description = "从ACE菜单中呼叫支援";};
	class callConstruct {description = "从ACE菜单中呼叫建造";};
	class resupply {description = "从弹药箱中补充弹药";};
	class breakdown {description = "将MCC箱子分解为补给";};
	class ACEdropAmmobox {description = "在ACE中投放MCC弹药箱";};
};

class evac
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\evac";
	#else
	file = "mcc\fnc\evac";
	#endif

	class evacDelete {description = "删除给定的车辆或其驾驶员";};
	class evacMove {description = "将车辆移动到选定的路点";};
	class evacSpawn {description = "生成一辆载有机组人员和炮手的车辆，并将其标记为撤离车辆";};
	class repairEvac {description = "修理撤离直升机";};
	class setEvac {description = "将一辆无人驾驶汽车设置为特定侧的撤离车辆";};
	class fastRopeLocal {description = "在客户端上处理快速绳降";};
};

class dynamicDialog
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\dynamicDialog";
	#else
	file = "mcc\fnc\dynamicDialog";
	#endif

	class initDynamicDialog {description = "初始化动态对话框";};
};