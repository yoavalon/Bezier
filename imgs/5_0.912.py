d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.long)

d.end()
