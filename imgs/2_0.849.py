d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
