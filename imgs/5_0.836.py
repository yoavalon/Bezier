d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
