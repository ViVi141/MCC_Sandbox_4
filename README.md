
# MCC Sandbox 4 社区维护版 v2.0.1 | MCC Sandbox 4 Community Edition v2.0.1

[![Steam创意工坊](https://img.shields.io/badge/Steam-Workshop-1b2838?logo=steam)](https://steamcommunity.com/sharedfiles/filedetails/?id=3439287971)
[![Github](https://img.shields.io/badge/github-ViVi141-brightgreen.svg)](https://github.com/ViVi141/MCC_Sandbox_4)
[![AGPL-3.0协议](https://img.shields.io/badge/License-AGPLv3-orange.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![版本](https://img.shields.io/badge/Version-2.0.1-orange.svg)](https://github.com/ViVi141/MCC_Sandbox_4/releases)

> 基于原版MCC Sandbox 4模组的社区维护版本（当前为v2.0.1版本）| Community-maintained fork of original MCC Sandbox 4 mod (Currently v2.0.1)

---

## 📖 项目背景 | Background

原项目 [MCC Sandbox 4](https://steamcommunity.com/sharedfiles/filedetails/?id=338988835) 自2020年起停止更新。原作为 **GPLv3 协议** 发布；本社区维护版本仓库当前 LICENSE 文件为 **AGPL-3.0**（许可变更需自行评估合规性）。我们创建此分支旨在：

- 🔄 延续模组兼容性维护
- 🛠️ 修复已知问题与崩溃
- ✨ 添加社区建议的新功能
- 📦 改善模组部署体验
- 🚀 **v2.0.1重大更新**：本地化支持与稳定性修复

**English Version:**  
The original [MCC Sandbox 4](https://steamcommunity.com/sharedfiles/filedetails/?id=338988835) mod has been unmaintained since 2020. The original is released under **GPLv3**; this repo's LICENSE file is currently **AGPL-3.0** (license change should be reviewed for compliance). We created this community edition to:

- 🔄 Continue compatibility maintenance
- 🛠️ Fix known issues and crashes
- ✨ Implement community-requested features
- 📦 Improve mod deployment experience
- 🚀 **v2.0.1 Major Update**: Localization support and stability fixes

### 🎯 v2.0.1 更新亮点 | v2.0.1 Update Highlights

本次更新是MCC Sandbox 4社区版历史上最大的一次升级，包含：

**稳定性与本地化** | **Stability & Localization**
- 修复已知问题与崩溃 | Fixed known issues and crashes
- 指挥官控制台与任务简报完全本地化 | Fully localized commander console and mission briefing
- 新增100+本地化键值 | Added 100+ localization keys

**本地化突破** | **Localization Breakthrough**
- 指挥官控制台完全中文化 | Fully localized commander console
- 任务简报系统多语言支持 | Multi-language support for mission briefing system
- 新增100+本地化键值 | Added 100+ localization keys

**稳定性提升** | **Stability Improvements**
- 修复15个已知问题 | Fixed 15 known issues
- 优化代码质量，提升兼容性 | Optimized code quality and improved compatibility
- 增强错误处理和调试功能 | Enhanced error handling and debugging capabilities

---

## 🚀 功能特性 | Features

### 当前改进 | Current Improvements
- ✅ 支持最新版游戏语法 |Support the latest version of game syntax
- ✅ 修复已知问题 | Fix known issues
- ✅ 中英双语本地化支持 | Support both Chinese and English localizations
- ❌ 性能优化系统已移除 | Performance optimization system (removed)
- ✅ 指挥官控制台修复 | Commander console fixes
- ✅ 全面本地化支持 | Comprehensive localization support
- ⚠️ **任务生成器（Mission Wizard）暂未正常使用** | **Mission Wizard is currently not functioning properly**

### 🆕 最新重大更新 | Latest Major Updates

#### v2.0.1 - 本地化与稳定性升级 | Localization & Stability Overhaul

> ⚠️ **注**：v2.0.0-pre 中曾实现性能监控/AI优化/对象池系统，后因稳定性问题于后续提交中**移除**（commit 63409b8）。当前版本不含性能优化系统。
> **Note**: The performance monitoring / AI optimization / object pooling systems implemented in v2.0.0-pre were **removed** in a later commit (63409b8) due to stability issues. The current version does not include them.

**🌐 全面本地化支持 | Comprehensive Localization Support**
- 指挥官控制台完全中文化 | Fully localized commander console
- 任务简报系统多语言支持 | Multi-language support for mission briefing system
- 自动生成内容本地化 | Localized auto-generated content
- 新增30+本地化键值 | Added 30+ localization keys

**🛠️ 任务生成系统优化 | Task Generation System Optimization**
- 异步任务创建队列 | Asynchronous task creation queue
- 任务创建重试机制 | Task creation retry mechanism
- 任务验证和清理系统 | Task validation and cleanup system
- 兼容性层确保向后兼容 | Compatibility layer ensures backward compatibility

**🐛 问题修复 | Bug Fixes**
- 修复任务生成超时问题 | Fixed task generation timeout issues
- 修复指挥官控制台显示问题 | Fixed commander console display issues
- 修复过时语法警告 | Fixed outdated syntax warnings
- 修复无限循环问题 | Fixed infinite loop issues
- 修复网络同步问题 | Fixed network synchronization issues

**📈 代码质量提升 | Code Quality Improvements**
- 替换过时的BIS_fnc_MP为remoteExec | Replaced outdated BIS_fnc_MP with remoteExec
- 优化短睡眠操作 | Optimized short sleep operations
- 改进错误处理机制 | Improved error handling mechanisms
- 增强调试和日志记录 | Enhanced debugging and logging

### 计划功能 | Roadmap
- 更多本地化覆盖 | Extended localization coverage
- 性能优化（视需求重新引入）| Performance optimization (re-introduce on demand)
- 社区功能建议 | Community feature suggestions

---

## 📋 更新日志 | Changelog

### v2.0.1 (2025-01-XX) - 本地化完善更新 | Localization Enhancement Update

#### 🌐 本地化改进 | Localization Improvements
- **硬编码文本本地化** | **Hardcoded Text Localization**
  - 检测并本地化所有硬编码显示文本 | Detected and localized all hardcoded display texts
  - 新增30+本地化键值（cutText, titleText, hint, description）| Added 30+ localization keys (cutText, titleText, hint, description)
  - 自动替换硬编码文本为本地化键值 | Automatically replaced hardcoded texts with localization keys
  - 支持简体中文和繁体中文翻译 | Support for Simplified and Traditional Chinese translations

#### ⚠️ 已知问题 | Known Issues
- **任务生成器（Mission Wizard）暂未正常使用** | **Mission Wizard is currently not functioning properly**
  - 任务生成器功能存在兼容性问题 | Mission Wizard has compatibility issues
  - 我们正在积极修复中 | We are actively working on fixing it
  - 预计在下一版本中修复 | Expected to be fixed in the next version

#### 🐛 问题修复 | Bug Fixes
- 修复硬编码文本导致的本地化问题 | Fixed localization issues caused by hardcoded texts
- 优化本地化键值命名规范 | Optimized localization key naming conventions

---

### v2.0.0-pre (2025-09-26) - 性能与本地化全面升级 | Performance & Localization Overhaul

#### 🆕 新增功能 | New Features
- **性能监控系统** | **Performance Monitoring System**
  - 实时CPU、内存、网络监控 | Real-time CPU, memory, network monitoring
  - 智能性能警告和建议 | Intelligent performance warnings and suggestions
  - 可配置的性能阈值 | Configurable performance thresholds
  - 用户友好的性能管理界面 | User-friendly performance management interface

- **AI优化系统** | **AI Optimization System**
  - 智能AI单位数量限制 | Intelligent AI unit count limiting
  - 距离基础模拟优化 | Distance-based simulation optimization
  - 动态AI技能调整 | Dynamic AI skill adjustment
  - 性能统计和监控 | Performance statistics and monitoring

- **对象池化系统** | **Object Pooling System**
  - 车辆、单位、标记对象池 | Vehicle, unit, marker object pools
  - 效果和辅助对象管理 | Effect and helper object management
  - 减少对象创建/销毁开销 | Reduced object creation/destruction overhead

- **任务管理系统** | **Task Management System**
  - 异步任务创建队列 | Asynchronous task creation queue
  - 任务创建重试机制 | Task creation retry mechanism
  - 任务验证和清理 | Task validation and cleanup
  - 兼容性层确保向后兼容 | Compatibility layer for backward compatibility

#### 🌐 本地化改进 | Localization Improvements
- **指挥官控制台** | **Commander Console**
  - 完全中文化界面 | Fully localized interface
  - 所有按钮和提示文本本地化 | All buttons and tooltips localized
  - 新增59个本地化键值 | Added 59 localization keys

- **任务简报系统** | **Mission Briefing System**
  - 简报类型本地化 | Briefing types localized
  - 自动生成内容多语言支持 | Multi-language support for auto-generated content
  - 新增30个简报相关本地化键值 | Added 30 briefing-related localization keys

- **性能监控界面** | **Performance Monitoring Interface**
  - 性能预设界面本地化 | Performance preset interface localized
  - 性能警告消息本地化 | Performance warning messages localized
  - 新增15个性能相关本地化键值 | Added 15 performance-related localization keys

#### 🐛 问题修复 | Bug Fixes
- 修复任务生成超时导致只生成部分实体的问题 | Fixed task generation timeout causing only partial entity generation
- 修复指挥官控制台滚轮菜单选项消失的问题 | Fixed commander console wheel menu option disappearing
- 修复过时语法警告（str比较、resize操作）| Fixed outdated syntax warnings (str comparison, resize operations)
- 修复4个无限循环问题 | Fixed 4 infinite loop issues
- 修复6个短睡眠操作优化 | Optimized 6 short sleep operations
- 修复过时网络调用（BIS_fnc_MP替换为remoteExec）| Fixed outdated network calls (BIS_fnc_MP replaced with remoteExec)

#### 📈 代码质量提升 | Code Quality Improvements
- 替换所有过时的BIS_fnc_MP为modern remoteExec | Replaced all outdated BIS_fnc_MP with modern remoteExec
- 优化短睡眠操作从0.01秒提升到0.1秒 | Optimized short sleep operations from 0.01s to 0.1s
- 改进错误处理机制和调试输出 | Improved error handling mechanisms and debug output
- 增强日志记录和性能统计 | Enhanced logging and performance statistics
- 添加任务创建统计和监控 | Added task creation statistics and monitoring

#### 🔧 技术改进 | Technical Improvements
- 新增性能配置系统 | Added performance configuration system
- 实现智能AI管理 | Implemented intelligent AI management
- 添加对象池管理 | Added object pool management
- 创建任务队列系统 | Created task queue system
- 实现兼容性层 | Implemented compatibility layer

#### 📊 统计信息 | Statistics
- **新增文件**: 8个 | **New files**: 8
- **修改文件**: 25个 | **Modified files**: 25
- **新增本地化键值**: 104个 | **New localization keys**: 104
- **修复问题**: 15个 | **Fixed issues**: 15
- **性能优化**: 10个 | **Performance optimizations**: 10

---

## 📥 安装指南 | Installation

> ⚠️ **重要提示** | **Important Notice**  
> - 当前版本为 v2.0.1，任务生成器（Mission Wizard）功能暂未正常使用，我们正在修复中。  
> - Current version is v2.0.1, Mission Wizard feature is currently not functioning properly and we are working on fixing it.

### Steam订阅（推荐）| Steam Subscription (Recommended)
1. 访问 [Steam创意工坊页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3439287971) | Visit the [Steam Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3439287971)
2. 点击 "Subscribe" 按钮 | Click "Subscribe" button
3. 启动游戏时自动加载 | The mod will be loaded automatically when you start the game

### 手动安装 | Manual Installation
```bash
git clone https://github.com/ViVi141/MCC_Sandbox_4.git
# Windows路径示例：
# Steam\steamapps\common\YourGame\Mods
# 
# Linux路径示例：
# ~/.local/share/YourGame/Mods
```

---

## 🤝 参与贡献 | Contribution

**我们欢迎以下贡献方式：**  
- 🐛 [提交问题报告](https://github.com/ViVi141/MCC_Sandbox_4/issues)
- 💡 [建议新功能](https://steamcommunity.com/workshop/discussions/?id=3439287971)
- 👨💻 提交代码PR
- 🌐 翻译改进

**English Version:**  
We welcome contributions through:  
- 🐛 [Issue reporting](https://github.com/ViVi141/MCC_Sandbox_4/issues)
- 💡 [Feature suggestions](https://steamcommunity.com/workshop/discussions/?id=3439287971)
- 👨💻 Code PRs
- 🌐 Translation improvements

---

## 📜 开源许可 | License

本项目基于 [shay_gman](https://steamcommunity.com/profiles/76561198007956840) 开发的 **MCC Sandbox 4**（原作为 **GPLv3 协议**）进行社区维护。当前仓库的 **LICENSE 文件为 AGPL-3.0**，与上游 GPLv3 的许可变更合规性需自行评估。可在以下位置查看：   |   
This project is a community-maintained fork of **MCC Sandbox 4** by [shay_gman](https://steamcommunity.com/profiles/76561198007956840), originally released under **GPLv3**. The current **LICENSE file in this repo is AGPL-3.0**; the compliance of this license change relative to upstream GPLv3 should be reviewed. See:  
- [仓库 LICENSE 文件](https://github.com/ViVi141/MCC_Sandbox_4/blob/master/LICENSE) | [Repo LICENSE file](https://github.com/ViVi141/MCC_Sandbox_4/blob/master/LICENSE)
- [GPLv3协议全文](https://www.gnu.org/licenses/gpl-3.0.html) | [GPLv3 license full text](https://www.gnu.org/licenses/gpl-3.0.html)
- [AGPLv3协议全文](https://www.gnu.org/licenses/agpl-3.0.html) | [AGPLv3 license full text](https://www.gnu.org/licenses/agpl-3.0.html)

**协议要求：**   |   
**License requirements:**  
- 分发与再分发需遵守仓库 LICENSE（当前为 AGPL-3.0）| Redistribution must comply with the repo LICENSE (currently AGPL-3.0)
- 本分支代码保持开源| The code in this branch remains open source
- 修改内容已明确标注| Modification content is clearly marked
- 包含完整的协议副本 | Contains a complete copy of the license

---

## 🙏 致谢 | Acknowledgments

- 特别感谢原开发者 [shay_gman](https://steamcommunity.com/profiles/76561198007956840) 的杰出工作 |Special thanks to the excellent work of the original developer [shay_gman](https://steamcommunity.com/profiles/76561198007956840)
- 当前维护者 [ViVi141](https://steamcommunity.com/profiles/76561199019580384/)| Current maintainer [ViVi141](https://steamcommunity.com/profiles/76561199019580384/)
- 使用本模组时请考虑给[原作品](https://steamcommunity.com/sharedfiles/filedetails/?id=338988835)点赞 ❤️| Please consider giving a thumbs-up to the [original mod](https://steamcommunity.com/sharedfiles/filedetails/?id=338988835) when using this mod

---

**📢 社区讨论**  | **Community Discussion**  
[Steam讨论区](https://steamcommunity.com/workshop/discussions/?id=3439287971) | [GitHub Issues](https://github.com/ViVi141/MCC_Sandbox_4/issues)
```


