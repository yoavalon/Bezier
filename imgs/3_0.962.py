d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
