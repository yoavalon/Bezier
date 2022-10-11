d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
