d = DslBezier()

d.position_pen(3,0)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)

d.end()
