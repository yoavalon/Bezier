d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
