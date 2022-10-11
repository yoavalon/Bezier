d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.position_pen(1,1)

d.end()
