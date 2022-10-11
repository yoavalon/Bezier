d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.SE, Length.medium)

d.end()
