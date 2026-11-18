# pairwise-depth-of-field

镜头从近景切远景时对焦拉风箱、前景边缘发虚、亮斑变成方块：CoC 用深度线性；对焦距离用屏幕中心；半分辨率 DOF 直接上采样；bokeh 用方核；散景高光被 clamp；近景和远景 CoC 同号；自动对焦每帧重置；相机切换不过渡；透明物体不写深度；VR 双眼对焦不同步。render/depth_of_field.py 是核心，tests/test_depth_of_field.py 15个红。要修的是：物理 CoC；对焦点采样；深度感知上采样；圆形散景；HDR 高光保留；近远焦分离；对焦保持；切换过渡；透明深度；双眼同步。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
