d = DslBezier()

d.position_pen(1,0)
d.position_pen(2,3)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.position_pen(3,3)

d.end()
