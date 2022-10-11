d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.N, Length.short)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,0)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)

d.end()
