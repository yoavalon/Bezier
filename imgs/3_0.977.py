d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
