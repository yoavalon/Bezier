d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)

d.end()
