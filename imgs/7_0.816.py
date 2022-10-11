d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)

d.end()
