d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.short)

d.end()
