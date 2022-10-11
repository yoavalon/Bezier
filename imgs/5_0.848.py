d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
