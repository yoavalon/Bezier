d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,0)

d.end()
