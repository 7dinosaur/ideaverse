---
title: Obsidian性能精简清单
tags:
  - 工具
  - Obsidian
status: 待办
date: 2026-09-22
---

# Obsidian 性能精简清单（2026-09-22）

> **排查结论**：实测渲染进程在会话期间持续占用 20~65% 单核（生命周期均值 50%），主嫌疑为 **Claudian 插件常驻轮询（代码含 250ms×2 轮询 + 网络心跳）+ 长会话渲染开销**；叠加因素：**库在机械硬盘（D 盘）**、32 个社区插件、25 个 CSS 片段、7 套主题、库内 git 大仓库（121MB）。已排除：杀软（Defender 实时防护关闭）、OneDrive（未同步该库）、CSS 动画（主题/片段 keyframes=0）。
> **已完成**：清理 `.obsidian` 遗留垃圾 ~28MB（plugins.zip 27MB、publish.css、12 个 .DS_Store 等），移至库外备份：`D:\hyper_ly\05_Personal\05_Obsidian\_obsidian-junk-backup-20260922\`（可随时恢复）。

## 一、最优先：验证 Claudian 面板影响（1 分钟）

- [ ] 折叠/关闭 Claudian 对话面板，静置 1 分钟，看任务管理器里 Obsidian CPU → 若降到 ~5% 内即为主因确认
- [ ] 长对话及时**新开会话**（当前对话已很长，继续用会加重界面渲染）
- [ ] 重启 Obsidian 清理残留 claude 进程（发现今早 9:57 的进程 10 小时未退出）

## 二、插件精简（设置 → 第三方插件）

**建议禁用——网络请求型**（渲染/操作时发外部请求，网络不畅时卡顿）：
- [ ] link-favicon（为外链抓 favicon）
- [ ] simple-embeds（抓推文/视频嵌入）
- [ ] obsidian-wikipedia
- [ ] convert-url-to-iframe（网页嵌入，最重）
- [ ] obsidian-auto-link-title（粘贴 URL 时抓网页标题）
- [ ] obsidian42-brat（测试版插件更新器；不用 beta 插件可关）
- [ ] obsidian-snippet-downloader（按需再启用）

**建议禁用——低频/可替代**：
- [ ] cmdr（命令增强）
- [ ] obsidian-zoom
- [ ] hotkeysplus-obsidian
- [ ] obsidian-file-link
- [ ] note-refactor-obsidian（低频）

**按需保留（不用则关）**：
- [ ] obsidian-icon-folder（文件树图标，1185 个图标文件 + 每次渲染开销；不在意图标可关）
- [ ] obsidian-hover-editor（悬浮预览增强）
- [ ] obsidian-excalidraw-plugin（在用则留）

**保留（常用/轻量）**：calendar、periodic-notes、dataview、tag-wrangler、table-editor-obsidian、pane-relief、obsidian-style-settings、darlal-switcher-plus、obsidian-advanced-uri、obsidian-list-callouts、obsidian-sortable、callout-manager、obsidian-text-format、hotkey-helper、nldates-obsidian、url-into-selection、realclaudian

## 三、CSS 片段精简（设置 → 外观 → CSS 片段，共 25 个启用）

- [ ] **MCL 三件套**（Wide Views / Multi Column / Gallery Cards）：只留实际在用的（笔记里用到多列语法就留对应文件，否则全禁——选择器复杂，滚动/打字有重排开销）
- [ ] **callout-* 系列（约 14 个）**：与 callout-manager 插件功能重叠，二选一；片段只留最常用的 3~5 个
- [ ] **cornell-* 4 个**：只留 v2 两个（banner-v2 / main-v2），禁用旧版
- [ ] **callout-content-TEST**：测试文件，直接禁用
- [ ] murf-ribbon-dragger、nick-milo-callouts：按需留一

## 四、主题精简（设置 → 外观 → 管理）

- [ ] 已装 7 套主题（Prism、Prism 个人版、Minimal、AnuPpuccin、LYT Mode、Cybertron 等），删除不用的，只留 Prism（在用）

## 五、后续可选（本次未执行，需要时在对话里说）

- [ ] git 仓库整理：`git gc` 打包 516 个松散对象，降低 `push.sh` 全量 add 的卡顿
- [ ] **库迁移到 C 盘 SSD**（三星 980，剩 37GB；库仅 300MB）——解决机械硬盘冷启动/开图/开 PDF 慢的结构性问题
- [ ] Windows 搜索索引排除该库（可选）

> 操作建议：每改一项后重启一次 Obsidian 观察效果；全部改完观察 1~2 天。任何一项都可随时恢复原样。
