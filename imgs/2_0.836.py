d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,0)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)

d.end()
