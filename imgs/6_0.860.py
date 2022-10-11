d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
