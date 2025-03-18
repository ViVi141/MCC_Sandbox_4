#define MCC_BRIEFING_TEXT 3055

class MCC_briefingDialogControls: MCC_RscControlsGroup
{
	idc = 512;
	x = 0.525 * safezoneW + safezoneX;
	y = 0.28 * safezoneH + safezoneY;
	w = 0.332292 * safezoneW;
	h = 0.23091 * safezoneH;

	class Controls
	{	
		class MCC_briefingDialogFrame: MCC_RscText
		{
			idc = -1;
			colorBackground[] = {0,0,0,0.9};

			w = 0.332292 * safezoneW;
			h = 0.23091 * safezoneH;
		};
		
		class MCC_briefingGeneratorTittle: MCC_RscText
		{
			idc = -1;

			text = "简报生成器:"; //--- ToDo: Localize;
			x = 0.108855 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.131249 * safezoneW;
			h = 0.0280063 * safezoneH;
			colorText[] = {0,1,1,1};
		};
		class MCC_briefingtext: MCC_RscText
		{
			idc = MCC_BRIEFING_TEXT;
			type = 2;

			x = 0.0630206 * safezoneW;
			y = 0.0549788 * safezoneH;
			w = 0.263542 * safezoneW;
			h = 0.0879657 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class MCC_briefingTextFrame: MCC_RscFrame
		{
			idc = -1;

			x = 0.0630206 * safezoneW;
			y = 0.0549788 * safezoneH;
			w = 0.263542 * safezoneW;
			h = 0.0879657 * safezoneH;
		};
		
		class MCC_briefingBriefing: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[0] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "情况"; //--- ToDo: Localize;
			x = 0.00572965 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "将给定文本添加到任务简报中"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class MCC_briefingEnemy: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[1] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "敌军"; //--- ToDo: Localize;
			x = 0.0286457 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.0721875 * safezoneW;
			h = 0.0280063 * safezoneH;
			tooltip = "将给定的文本添加到任务的敌军情报中"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_briefingFriendly: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[2] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "友军"; //--- ToDo: Localize;
			x = 0.103125 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.0721875 * safezoneW;
			h = 0.0280063 * safezoneH;
			tooltip = "将给定的文本添加到任务的友军信息中l"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_briefingMission: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[3] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "任务"; //--- ToDo: Localize;
			x = 0.00572965 * safezoneW;
			y = 0.0549788 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "将给定文本添加到任务概述中"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class MCC_briefingSpecial: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[4] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "特殊任务"; //--- ToDo: Localize;
			x = 0.177605 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.0721875 * safezoneW;
			h = 0.0280063 * safezoneH;
			tooltip = "将给定文本添加到任务的特殊任务中"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_briefingSupport: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL ("[5] execVM '"+MCCPATH+"mcc\pop_menu\briefing.sqf'");

			text = "支持"; //--- ToDo: Localize;
			x = 0.252084 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.0721875 * safezoneW;
			h = 0.0280063 * safezoneH;
			tooltip = "将给定的文本添加到任务的支持信息中"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_briefingClose: MCC_RscButtonMenu
		{
			idc = -1;
			onButtonClick = "((uiNamespace getVariable 'MCC_groupGen_Dialog') displayCtrl 512) ctrlShow false";

			text = "关闭"; //--- ToDo: Localize;
			x = 0.14323 * safezoneW;
			y = 0.197923 * safezoneH;
			w = 0.0721875 * safezoneW;
			h = 0.0280063 * safezoneH;
		};
	};
};
	

