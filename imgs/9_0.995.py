d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)

d.end()
