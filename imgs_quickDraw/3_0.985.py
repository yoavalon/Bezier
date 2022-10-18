d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)

d.end()
