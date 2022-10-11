d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
