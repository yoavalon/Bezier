d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)

d.end()
