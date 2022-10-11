d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,3)
d.straight_line(Direction.SE, Length.medium)

d.end()
