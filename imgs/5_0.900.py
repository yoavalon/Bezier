d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.N, Length.long)

d.end()
