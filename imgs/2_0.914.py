d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.short)

d.end()
