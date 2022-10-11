d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,3)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,0)

d.end()
