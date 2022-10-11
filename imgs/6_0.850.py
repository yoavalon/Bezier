d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.N, Length.medium)

d.end()
