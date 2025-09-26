class MCC_taskMonitorDialog {
	idd = 9001;
	movingEnable = 1;
	enableSimulation = 1;
	
	class controlsBackground {
		class Background: MCC_RscText {
			idc = -1;
			x = 0.6 * safezoneW + safezoneX;
			y = 0.1 * safezoneH + safezoneY;
			w = 0.35 * safezoneW;
			h = 0.4 * safezoneH;
			colorBackground[] = {0,0,0,0.8};
		};
		
		class Title: MCC_RscText {
			idc = 1001;
			text = "$STR_MCC_TASK_MONITOR_TITLE";
			x = 0.6 * safezoneW + safezoneX;
			y = 0.1 * safezoneH + safezoneY;
			w = 0.35 * safezoneW;
			h = 0.05 * safezoneH;
			colorBackground[] = {0,0.5,0,0.8};
			colorText[] = {1,1,1,1};
			sizeEx = 0.04;
		};
	};
	
	class controls {
		class StatsList: MCC_RscListbox {
			idc = 1501;
			x = 0.62 * safezoneW + safezoneX;
			y = 0.17 * safezoneH + safezoneY;
			w = 0.31 * safezoneW;
			h = 0.25 * safezoneH;
			colorBackground[] = {0,0,0,0.5};
			colorText[] = {1,1,1,1};
		};
		
		class RefreshButton: MCC_RscButton {
			idc = 1601;
			text = "$STR_MCC_TASK_MONITOR_REFRESH";
			x = 0.62 * safezoneW + safezoneX;
			y = 0.43 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "[] call MCC_fnc_refreshTaskStats;";
		};
		
		class CleanupButton: MCC_RscButton {
			idc = 1602;
			text = "$STR_MCC_TASK_MONITOR_CLEANUP";
			x = 0.73 * safezoneW + safezoneX;
			y = 0.43 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "[] call MCC_fnc_emergencyCleanup;";
		};
		
		class CloseButton: MCC_RscButton {
			idc = 1603;
			text = "$STR_MCC_TASK_MONITOR_CLOSE";
			x = 0.84 * safezoneW + safezoneX;
			y = 0.43 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "closedialog 0;";
		};
	};
};
