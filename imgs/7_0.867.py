d = DslBezier()

d.position_pen(2,3)
d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,2)

d.end()
