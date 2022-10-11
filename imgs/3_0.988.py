d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)

d.end()
