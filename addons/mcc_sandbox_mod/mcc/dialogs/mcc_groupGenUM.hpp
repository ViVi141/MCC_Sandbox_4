#define MCC_UM_LIST 3069
#define MCC_UM_PIC 3070
#define MCC_UM_KICK 3076
#define MCC_UM_BAN 3077

class MCC_UMDialogControls:MCC_RscControlsGroup
{
	idc = 519;
	x = 0.471354 * safezoneW + safezoneX;
	y = 0.620953 * safezoneH + safezoneY;
	w = 0.469792 * safezoneW;
	h = 0.164936 * safezoneH;

	class Controls
	{
		class MCC_UMDialogControlsFrame: MCC_RscText
		{
			idc = -1;
			text = "";
			colorBackground[] = { 0.120, 0.120, 0.120,1};

			w = 0.469792 * safezoneW;
			h = 0.164936 * safezoneH;
		};

		class MCC_UMList: MCC_RscListbox
		{
			idc = MCC_UM_LIST;
			rowHeight = 0.022;
			style = MCCLB_MULTI;
			colorBackground[] = { 0, 0, 0,1};
			onSetFocus = "MCC_UMFocus = true";
			onKillFocus = "MCC_UMFocus = false";
			onLBSelChanged = __EVAL("[4] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");
			onMouseButtonUp = __EVAL("[8,_this] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";

			x = 0.00572965 * safezoneW;
			y = 0.0439828 * safezoneH;
			w = 0.160417 * safezoneW;
			h = 0.109957 * safezoneH;
		};
		class MCC_UMUnits: MCC_RscToolbox
		{
			idc = -1;
			strings[] = {"单位","小组"};
			rows = 1;
			columns = 2;
			values[] = {0,1};
			onToolBoxSelChanged = "MCC_UMUnit = (_this select 1);";

			x = 0.00572965 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "在单位和小组之间切换显示"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMTeleport: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[0] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "传送"; // 汉化
			x = 0.171875 * safezoneW;
			y = 0.0329868 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "传送选定的单位"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMHijak: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[2] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "劫持"; // 汉化
			x = 0.171875 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "劫持选定的单位，仅对非玩家单位有效"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMMark: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[3] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "追踪单位"; // 汉化
			x = 0.171875 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "在地图上切换所有单位的追踪显示"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMbroadcast: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[11] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "广播"; // 汉化
			x = 0.171875 * safezoneW;
			y = 0.0659738 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "向所有玩家广播实时画面，持续15秒"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMDelete: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[12] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "删除"; // 汉化
			x = 0.234896 * safezoneW;
			y = 0.0659738 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "删除选定的单位或小组"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMJoin: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[13] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "加入"; // 汉化
			x = 0.234896 * safezoneW;
			y = 0.0329868 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "将单位或小组加入另一个单位或小组"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMHALO: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[9] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "高跳低开"; // 汉化
			x = 0.234896 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "对当前选定的单位执行高跳低开"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMParachute: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[10] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "跳伞"; // 汉化
			x = 0.234896 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "对当前选定的单位执行跳伞"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMKick: MCC_RscButton
		{
			idc = MCC_UM_KICK;
			onButtonClick = __EVAL ("[15] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "踢出"; // 汉化
			x = 0.171875 * safezoneW;
			y = 1.63913e-008 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "将选定的玩家踢出服务器"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMBan: MCC_RscButton
		{
			idc = MCC_UM_BAN;
			onButtonClick = __EVAL ("[16] execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um.sqf'");

			text = "封禁"; // 汉化
			x = 0.234896 * safezoneW;
			y = 1.63913e-008 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "将选定的玩家封禁出服务器"; // 汉化
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class MCC_UMListFrame: MCC_RscFrame
		{
			idc = -1;

			x = 0.00572965 * safezoneW;
			y = 0.0439828 * safezoneH;
			w = 0.160417 * safezoneW;
			h = 0.109957 * safezoneH;
		};
		class MCC_UMhint: MCC_RscText
		{
			idc = -1;

			text = "*Ctrl/Shift 多选"; // 汉化
			x = 0.0791667 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.0916667 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.55)";
		};
		class MCC_PIPUm: MCC_RscPicture
		{
			idc = MCC_UM_PIC;
			colorBackground[] = { 0, 0, 0,1};

			text = "#(argb,256,256,1)r2t(rendertarget10,1.0);"; //--- ToDo: Localize;
			x = 0.292188 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.171875 * safezoneW;
			h = 0.120953 * safezoneH;
		};
		class MCC_PIPUmFrame: MCC_RscFrame
		{
			idc = -1;

			x = 0.292188 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.171875 * safezoneW;
			h = 0.120953 * safezoneH;
		};
		class MCC_PIPviewMod: MCC_RscToolbox
		{
			idc = -1;
			strings[] = {"常规","夜视","热成像"};
			rows = 1;
			columns = 3;
			values[] = {0,1,3};
			onToolBoxSelChanged = __EVAL("_this execVM '"+MCCPATH+"mcc\general_scripts\unitManage\um_camView.sqf'");

			x = 0.292188 * safezoneW;
			y = 0.134808 * safezoneH;
			w = 0.171875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
	};
};
