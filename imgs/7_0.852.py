d = DslBezier()

d.position_pen(2,3)
d.position_pen(1,3)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.position_pen(3,2)

d.end()
