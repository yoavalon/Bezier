d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.medium)

d.end()
