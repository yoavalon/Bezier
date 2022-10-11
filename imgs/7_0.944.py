d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)

d.end()
