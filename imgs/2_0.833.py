d = DslBezier()

d.position_pen(2,2)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,3)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.long)

d.end()
