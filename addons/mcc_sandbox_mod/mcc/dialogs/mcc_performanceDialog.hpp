class MCC_PerformanceDialog {
	idd = 12345;
	movingEnable = false;
	onLoad = "[] call MCC_fnc_displayPerformanceInfo";
	
	class controlsBackground {
		class Background: MCC_RscText {
			idc = -1;
			x = 0.3 * safezoneW + safezoneX;
			y = 0.25 * safezoneH + safezoneY;
			w = 0.4 * safezoneW;
			h = 0.5 * safezoneH;
			colorBackground[] = {0,0,0,0.8};
		};
		
		class Title: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_TITLE";
			x = 0.3 * safezoneW + safezoneX;
			y = 0.25 * safezoneH + safezoneY;
			w = 0.4 * safezoneW;
			h = 0.05 * safezoneH;
			colorBackground[] = {0,0,0,0.9};
			colorText[] = {1,1,1,1};
			sizeEx = 0.04;
		};
	};
	
	class controls {
		class CPUUsage: MCC_RscText {
			idc = 1000;
			text = "CPU Usage: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.32 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class MemoryUsage: MCC_RscText {
			idc = 1001;
			text = "Memory Usage: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.36 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class NetworkOps: MCC_RscText {
			idc = 1002;
			text = "Network Operations: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.4 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class ObjectCount: MCC_RscText {
			idc = 1003;
			text = "Object Count: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.44 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class AICount: MCC_RscText {
			idc = 1004;
			text = "AI Count: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.48 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class LoopCount: MCC_RscText {
			idc = 1005;
			text = "Loop Count: 0";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.52 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class Recommendations: MCC_RscStructuredText {
			idc = 1006;
			text = "Performance Recommendations:";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.56 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.1 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class CloseButton: MCC_RscButton {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_CLOSE";
			x = 0.5 * safezoneW + safezoneX;
			y = 0.68 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "closeDialog 0";
		};
	};
};
