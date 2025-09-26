class MCC_PerformanceSettings {
	idd = 12346;
	movingEnable = false;
	onLoad = "[] call MCC_fnc_openPerformanceSettings";
	
	class controlsBackground {
		class Background: MCC_RscText {
			idc = -1;
			x = 0.25 * safezoneW + safezoneX;
			y = 0.2 * safezoneH + safezoneY;
			w = 0.5 * safezoneW;
			h = 0.6 * safezoneH;
			colorBackground[] = {0,0,0,0.8};
		};
		
		class Title: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_SETTINGS_TITLE";
			x = 0.25 * safezoneW + safezoneX;
			y = 0.2 * safezoneH + safezoneY;
			w = 0.5 * safezoneW;
			h = 0.05 * safezoneH;
			colorBackground[] = {0,0,0,0.9};
			colorText[] = {1,1,1,1};
			sizeEx = 0.04;
		};
	};
	
	class controls {
		// CPU Threshold
		class CPULabel: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_CPU_THRESHOLD";
			x = 0.27 * safezoneW + safezoneX;
			y = 0.28 * safezoneH + safezoneY;
			w = 0.2 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class CPUInput: MCC_RscEdit {
			idc = 2001;
			text = "80";
			x = 0.5 * safezoneW + safezoneX;
			y = 0.28 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.03 * safezoneH;
		};
		
		// Memory Threshold
		class MemoryLabel: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_MEMORY_THRESHOLD";
			x = 0.27 * safezoneW + safezoneX;
			y = 0.32 * safezoneH + safezoneY;
			w = 0.2 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class MemoryInput: MCC_RscEdit {
			idc = 2002;
			text = "70";
			x = 0.5 * safezoneW + safezoneX;
			y = 0.32 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.03 * safezoneH;
		};
		
		// AI Limit
		class AILabel: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_AI_LIMIT";
			x = 0.27 * safezoneW + safezoneX;
			y = 0.36 * safezoneH + safezoneY;
			w = 0.2 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class AIInput: MCC_RscEdit {
			idc = 2003;
			text = "50";
			x = 0.5 * safezoneW + safezoneX;
			y = 0.36 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.03 * safezoneH;
		};
		
		// Object Pooling
		class PoolingLabel: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_OBJECT_POOLING";
			x = 0.27 * safezoneW + safezoneX;
			y = 0.4 * safezoneH + safezoneY;
			w = 0.2 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class PoolingCheckbox: MCC_RscCheckbox {
			idc = 2004;
			x = 0.5 * safezoneW + safezoneX;
			y = 0.4 * safezoneH + safezoneY;
			w = 0.02 * safezoneW;
			h = 0.03 * safezoneH;
		};
		
		// Monitoring
		class MonitoringLabel: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_MONITORING";
			x = 0.27 * safezoneW + safezoneX;
			y = 0.44 * safezoneH + safezoneY;
			w = 0.2 * safezoneW;
			h = 0.03 * safezoneH;
			colorText[] = {1,1,1,1};
		};
		
		class MonitoringCheckbox: MCC_RscCheckbox {
			idc = 2005;
			x = 0.5 * safezoneW + safezoneX;
			y = 0.44 * safezoneH + safezoneY;
			w = 0.02 * safezoneW;
			h = 0.03 * safezoneH;
		};
		
		// Buttons
		class ApplyButton: MCC_RscButton {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_APPLY";
			x = 0.3 * safezoneW + safezoneX;
			y = 0.5 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "[] call MCC_fnc_applyPerformanceSettings;";
		};
		
		class ResetButton: MCC_RscButton {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_RESET";
			x = 0.45 * safezoneW + safezoneX;
			y = 0.5 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "[] call MCC_fnc_resetPerformanceConfig;";
		};
		
		class CloseButton: MCC_RscButton {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_CLOSE";
			x = 0.6 * safezoneW + safezoneX;
			y = 0.5 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "closeDialog 0;";
		};
	};
};
