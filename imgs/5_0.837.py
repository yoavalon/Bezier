d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
