class ui
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\ui\fnc";
	#else
	file = "mcc\ui\fnc";
	#endif

	class countDownLine	{description = "创建一个填充等待栏-由BIS制作所有积分。";};
	class drawLine	{description = " 在地图上两点之间画一个箭头。";};
	class drawArrow	{description = " 展开：在地图上两点之间局部画一条线。";};
	class drawBox	{description = "在地图上两点之间局部画一个方框。";};
	class trackUnits	{description = "在给定的地图显示上跟踪单位";};
	class camp_showOSD	{description = "显示玩家OSD";};
	class curatorInitLine	{description = "处理MCC的管理员初始化行";};
	class initDispaly		{description = "处理MCC的显示初始化";};
	class makeMarker		{description = "创建标记";};
	class createMCCZones	{description = "“在本地创建MCC区域";};
	class initCuratorAttribute	{description = "Init MCC的策划属性";};
	class interactProgress	{description = "为玩家创建进度条和动画";};
	class keyDown			{description = "手柄按键向下/按键向上EH";};
	class help				{description = "显示工具提示";};
	class playerStats		{description = "在RS中显示玩家统计数据";};
	class getKeyFromAction 	{description = "从CfgActions中定义的操作中获取密钥名称";};
	class setIDCText 		{description = "将文本设置为当前IDC";};
	class CBAInteractionKeybind {description = "处理CBA键盘绑定以进行交互";};
	class CBAKeybinds {description = "处理CBA键盘绑定";};
	class getKeyFromCBA {description = "从CBA键盘绑定中获得漂亮的名称";};
	class getGroupIconData {description = "获取组图标取决于组类型和大小";};
	class 3Dcredits	{};
	class musicTrigger {description = "在所有客户端触发器上执行音乐或声音";};
	class tagSystem {description = "初始化MCC 3d标记-标记系统。标记敌人时添加3D标记";};
	class formatNumber {description = "设置一个数字的格式，加上几千个逗号";};
	class checkBox {description = "处理复选框控件UI";};
};