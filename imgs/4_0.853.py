d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,0)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)

d.end()
