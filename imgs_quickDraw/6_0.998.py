d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,0)

d.end()
