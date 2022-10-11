d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
