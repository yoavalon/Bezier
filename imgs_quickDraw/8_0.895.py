d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)
d.position_pen(1,2)

d.end()
