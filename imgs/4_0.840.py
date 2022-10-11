d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.position_pen(1,3)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.E, Length.long)
d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
